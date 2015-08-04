/**
* NavbarController
* @namespace fcbp.navbar.controllers
*/
(function () {
  'use strict';

  angular
    .module('fcbp.navbar.controllers')
    .controller('NavbarController', NavbarController);

  NavbarController.$inject = ['$scope', 'Authentication'];

  /**
  * @namespace NavbarController
  */
  function NavbarController($scope, Authentication) {
    var vm = this;

    vm.logout = logout;

    /**
    * @name logout
    * @desc Log the user out
    * @memberOf fcbp.navbar.controllers.NavbarController
    */
    function logout() {
      Authentication.logout();
    }
  }
})();