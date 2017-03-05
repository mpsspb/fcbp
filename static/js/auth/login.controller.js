/**
* LoginController
* @namespace fcbp.auth.controllers
*/
(function () {
  'use strict';

  angular
    .module('fcbp.auth.controllers')
    .controller('LoginController', LoginController);

  LoginController.$inject = ['$http', '$location', '$localStorage', 'Authentication'];

  /**
  * @namespace LoginController
  */
  function LoginController($http, $location, $localStorage, Authentication) {
    var vm = this;

    vm.login = login;

    activate();

    /**
    * @name activate
    * @desc Actions to be performed when this controller is instantiated
    * @memberOf fcbp.authentication.controllers.LoginController
    */
    function activate() {
      // If the user is authenticated, they should not be here.
      if (Authentication.isAuthenticated()) {
        $location.url('/');
      }
    }

    /**
    * @name login
    * @desc Log the user in
    * @memberOf fcbp.authentication.controllers.LoginController
    */
    function login() {
      $http.post('/api/v1/users/login/', {
        username: vm.username, password: vm.password
      }).then(loginSuccessFn, loginErrorFn);

      /**
       * @name loginSuccessFn
       * @desc Set the authenticated account and redirect to index
       */
      function loginSuccessFn(data, status, headers, config) {
        $localStorage.user = JSON.stringify(data.data);
        window.location = '/';
      }

      /**
       * @name loginErrorFn
       * @desc Log "Epic failure!" to the console
       */
      function loginErrorFn(data, status, headers, config) {
        console.error('Epic failure!');
      }
    }
  }
})();