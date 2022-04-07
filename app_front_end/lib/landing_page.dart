import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'common/question.dart';

import 'urls.dart';
import 'dart:convert';

class LandingPage extends StatefulWidget {
  static String routeName = '/land';
  String _sessionID;

  LandingPage(this._sessionID);

  @override
  _LandingPageState createState() => _LandingPageState(this._sessionID);
}

class _LandingPageState extends State<LandingPage> {
  TextEditingController _answerController = TextEditingController();

  String _sessionID = 'Invalid Session ID';
  String _currentQuestion = 'Default Question';
  int _questionIndex = 0;

  _LandingPageState(this._sessionID);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Check In App Landing Page"),
        leading: Container(),
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
                  this._currentQuestion,
                  style: TextStyle(
                    fontSize: 60,
                  ),
                ),
              ],
            ),
            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              crossAxisAlignment: CrossAxisAlignment.center,
              children: [
                Container(
                  width: 1000,
                  height: 100,
                  child: Center(
                    child: TextField(
                      controller: _answerController,
                      textAlign: TextAlign.center,
                      decoration: InputDecoration(
                        hintText: "Answer the question",
                        hintStyle: TextStyle(fontSize: 25),
                      ),
                      style: TextStyle(fontSize: 25),
                    ),
                  ),
                ),
              ],
            ),
            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              crossAxisAlignment: CrossAxisAlignment.center,
              children: [
                Container(
                  width: 1000,
                  height: 100,
                  child: Center(
                    child: SizedBox(
                      height: 50,
                      width: 100,
                      child: RaisedButton(
                        onPressed: _submit,
                        child: Text(
                          'Submit',
                          style: TextStyle(
                            color: Colors.white,
                          ),
                        ),
                        color: Colors.blue,
                      ),
                    ),
                  ),
                ),
              ],
            ),
          ],
        ),
      ),
    );
  }

  void _submit() {
    //Read the answer to the question
    String answer = _answerController.text;

    // Persist the answer to the question
    _persistAnswer(answer).then((success) => {
          // Handle status of persist
          if (!success)
            {
              //  Fail in some way
              print('Persist Answer failed!')
            },

          // Advance the question index to the next question
          _questionIndex++,

          // Retrieve the next qeustion
          _retrieveQuestion(_questionIndex).then(
            (value) => {
              this.setState(() {
                if (value == '-1') {
                  this._currentQuestion = "Thanks, we are done!";
                } else {
                  this._currentQuestion = value;
                }
              })
            },
          )
        });
  }

  Future<bool> _persistAnswer(String answer) async {
    var uri = Uri.parse(URLs.UI_BACK_END_STORE_ANSWER_URL);

    uri = uri.replace(
      queryParameters: <String, String>{
        URLs.SESSION_ID_QUERY: this._sessionID,
        URLs.QUESTION_QUERY: this._currentQuestion,
        URLs.ANSWER_QUERY: answer
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

  Future<String> _retrieveQuestion(int questionIndex) async {
    String last_answer = _answerController.text;

    var uri = Uri.parse(URLs.UI_BACK_END_RETRIEVE_QUESTIONS_URL);

    uri = uri.replace(
      queryParameters: <String, String>{
        URLs.SESSION_ID_QUERY: this._sessionID,
        URLs.QUESTION_INDEX_QUERY: questionIndex.toString(),
        URLs.ANSWER_QUERY: last_answer
      },
    );

    final response = await http.get(uri);

    if (response.statusCode == 200) {
      return Question.fromJson(jsonDecode(response.body)).getQuestion();
    } else {
      //Fail in some way
      return 'Unable to Retrieve Question!';
    }
  }

  @override
  void initState() {
    super.initState();
    _retrieveQuestion(_questionIndex).then(
      (value) => {
        this.setState(() {
          this._currentQuestion = value;
        })
      },
    );
  }

  @override
  void dispose() {
    _answerController.dispose();
    super.dispose();
  }
}
