class URLs {
  //URLs
  static String UI_BACK_END_RETRIEVE_QUESTIONS_URL =
      'http://localhost:5001/retrieve-question';
  static String UI_BACK_END_STORE_ANSWER_URL =
      'http://localhost:5001/store-answer';
  static String UI_BACK_END_STORE_USER_PROFILE_INFO =
      'http://localhost:5001/save-user-profile';
  static String UI_BACK_END_RETRIEVE_USER_PROFILE_INFO =
      'http://localhost:5001/retrieve-user-profile';

  //Query Parameters
  static String ANSWER_QUERY = 'answer';
  static String QUESTION_QUERY = 'question';
  static String QUESTION_INDEX_QUERY = 'index';
  static String SESSION_ID_QUERY = 'session_id';
  static String EMAIL_QUERY = 'email';
  static String CHECK_IN_TIME_QUERY = 'check_in_time';
}
