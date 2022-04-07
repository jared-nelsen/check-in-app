import 'dart:convert';

import 'package:app_front_end/urls.dart';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

import 'utilities.dart';

class ManageUserProfile extends StatefulWidget {
  static String routeName = '/user-profile';

  @override
  _ManageUserProfileState createState() => _ManageUserProfileState();
}

class _ManageUserProfileState extends State<ManageUserProfile> {
  TextEditingController _emailController = TextEditingController();
  TextEditingController _checkInTimeController = TextEditingController();

  final _emailFormKey = GlobalKey<FormState>();
  final _checkInTimeFormKey = GlobalKey<FormState>();

  TimeOfDay _checkInTime = TimeOfDay.now();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("User Management"),
      ),
      body: Container(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          crossAxisAlignment: CrossAxisAlignment.center,
          children: [
            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                Text(
                  'User Profile Settings',
                  style: TextStyle(
                    fontSize: 30,
                  ),
                ),
              ],
            ),
            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              crossAxisAlignment: CrossAxisAlignment.center,
              children: [
                Container(
                  width: 500,
                  height: 100,
                  child: Center(
                    child: Form(
                      key: _emailFormKey,
                      child: TextFormField(
                        controller: _emailController,
                        textAlign: TextAlign.center,
                        decoration: InputDecoration(
                          helperText: "Email",
                          hintText: "Email",
                          hintStyle: TextStyle(fontSize: 25),
                        ),
                        style: TextStyle(fontSize: 25),
                        validator: (value) {
                          if (value.isEmpty) {
                            return 'Please enter an email address';
                          }
                          return null;
                        },
                      ),
                    ),
                  ),
                ),
              ],
            ),
            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              crossAxisAlignment: CrossAxisAlignment.center,
              children: [
                Text(
                  'Check In Time Settings',
                  style: TextStyle(
                    fontSize: 30,
                  ),
                ),
              ],
            ),
            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              crossAxisAlignment: CrossAxisAlignment.center,
              children: [
                Container(
                  width: 500,
                  height: 100,
                  child: Center(
                    child: Form(
                      key: _checkInTimeFormKey,
                      child: TextFormField(
                        enabled: false,
                        controller: _checkInTimeController,
                        textAlign: TextAlign.center,
                        decoration: InputDecoration(
                          helperText: "Check In Time",
                          hintText: "Check In Time",
                          hintStyle: TextStyle(fontSize: 25),
                        ),
                        style: TextStyle(fontSize: 25),
                        validator: (value) {
                          if (value.isEmpty) {
                            return 'Please select a check in time';
                          }
                          return null;
                        },
                      ),
                    ),
                  ),
                ),
                RaisedButton(
                  onPressed: _pickCheckInTime,
                  color: Colors.blue,
                  child: Text(
                    "Update Time",
                    style: TextStyle(color: Colors.white),
                  ),
                ),
              ],
            ),
            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              crossAxisAlignment: CrossAxisAlignment.center,
              children: [
                RaisedButton(
                  color: Colors.blue,
                  onPressed: _submit,
                  child: Text(
                    'Update',
                    style: TextStyle(color: Colors.white),
                  ),
                )
              ],
            ),
          ],
        ),
      ),
    );
  }

  @override
  void initState() {
    super.initState();
    _loadUserProfile().then(
      (success) => {
        if (!success)
          {Utilities.showFailureDialog(context, "Failed to load user profile!")}
      },
    );
  }

  Future<bool> _loadUserProfile() async {
    var uri = Uri.parse(URLs.UI_BACK_END_RETRIEVE_USER_PROFILE_INFO);

    //Here I would add query params to send auth

    final response = await http.get(uri);

    Map<String, dynamic> responseJson = jsonDecode(response.body);

    String email = responseJson['email'];
    String checkInTimeString = responseJson['check_in_time'];

    if (email == null || checkInTimeString == null) {
      return false;
    }

    DateTime checkInTimeDateTime = DateTime.parse(checkInTimeString);
    TimeOfDay checkInTimeTimeOfDay =
        TimeOfDay.fromDateTime(checkInTimeDateTime);
    final localizations = MaterialLocalizations.of(context);
    final checkInTime = localizations.formatTimeOfDay(checkInTimeTimeOfDay);

    _emailController.text = email;
    _checkInTimeController.text = checkInTime;

    return true;
  }

  Future<bool> _persistUserProfileInfo(
      String email, String checkInTimeISO8601) async {
    var uri = Uri.parse(URLs.UI_BACK_END_STORE_USER_PROFILE_INFO);

    uri = uri.replace(
      queryParameters: <String, String>{
        URLs.EMAIL_QUERY: email,
        URLs.CHECK_IN_TIME_QUERY: checkInTimeISO8601
      },
    );

    final response = await http.get(uri);

    if (response.statusCode == 200) {
      return true;
    } else {
      //Fail in some way
      return false;
    }
  }

  _submit() {
    // Validate Forms
    if (!_emailFormKey.currentState.validate()) {
      return;
    }

    if (!_checkInTimeFormKey.currentState.validate()) {
      Utilities.showFailureDialog(context, "Please select a check in time");
      return;
    }

    String email = _emailController.text;

    String checkInTime = _makeCheckInTimeString();

    _persistUserProfileInfo(email, checkInTime).then(
      (succcess) => {
        if (!succcess)
          {
            //Fail in some way
            print('Persist user profile failed!')
          }
        else
          {
            Utilities.showConfirmationDialog(context, "Save User Profile",
                "User Profile saved successfully!")
          }
      },
    );
  }

  _pickCheckInTime() async {
    TimeOfDay t =
        await showTimePicker(context: context, initialTime: _checkInTime);
    _checkInTimeController.text = t.format(context);
  }

  String _makeCheckInTimeString() {
    // Get the time of day text from the controller
    String timeOfDayText = _checkInTimeController.text;

    //Normalize time of day text
    timeOfDayText = timeOfDayText.replaceAll(' AM', '');
    timeOfDayText = timeOfDayText.replaceAll(' PM', '');

    // Create a time of day object from the text
    TimeOfDay t = TimeOfDay(
      hour: int.parse(timeOfDayText.split(":")[0]),
      minute: int.parse(timeOfDayText.split(":")[1]),
    );

    // Create a final date time representing the check in time
    final now = new DateTime.now();
    DateTime checkInTime =
        new DateTime(now.year, now.month, now.day, t.hour, t.minute);

    // Convert DateTime to ISO 8601
    String finalCheckInTime = checkInTime.toIso8601String();

    //Return it
    return finalCheckInTime;
  }
}
