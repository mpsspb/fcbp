(function () {
  'use strict';

  angular
    .module('fcbp',[
      'fcbp.routes',
      'fcbp.navbar',
      'fcbp.auth',
      'fcbp.layout',
      'fcbp.products',
      'fcbp.clients',
      'fcbp.employees',
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
 
})();