(function () {
  'use strict';

  angular
    .module('fcbp', [
      'fcbp.routes',
      'fcbp.layout',
      'fcbp.auth',
    ])
    .run(run);

  run.$inject = ['$http'];

    /**
    * @name run
    * @desc Update xsrf $http headers to align with Django's defaults
    */
    function run($http) {
      $http.defaults.xsrfHeaderName = 'X-CSRFToken';
      $http.defaults.xsrfCookieName = 'csrftoken';
    };

  angular
    .module('fcbp.routes', ['ngRoute']);
 
})();