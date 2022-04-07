import 'package:app_front_end/landing_page.dart';
import 'package:app_front_end/manage_user_profile.dart';
import 'package:flutter/material.dart';

import 'home_page.dart';

void main() {
  runApp(CheckInApp());
}

class CheckInApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        primarySwatch: Colors.blue,
        visualDensity: VisualDensity.adaptivePlatformDensity,
      ),
      initialRoute: HomePage.routeName,
      routes: {
        HomePage.routeName: (context) => HomePage(),
        ManageUserProfile.routeName: (context) => ManageUserProfile(),
      },
      onGenerateRoute: (settings) {
        String specificRoute = settings.name.substring(0, 5);

        if (specificRoute == LandingPage.routeName) {
          String sessionID = Uri.parse(settings.name).queryParameters['id'];

          if (sessionID == null ||
              sessionID.isEmpty ||
              sessionID.length != 32) {
            //Maybe navigate to an error screen
            return MaterialPageRoute(
              builder: (context) {
                return HomePage();
              },
            );
          }

          return MaterialPageRoute(
            builder: (context) {
              return LandingPage(sessionID);
            },
          );
        }
      },
    );
  }
}
