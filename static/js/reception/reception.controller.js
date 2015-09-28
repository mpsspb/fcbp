/**
* ReceptionController
* @namespace fcbp.layout.controllers
*/
(function () {
  'use strict';

  angular
    .module('fcbp.layout.controllers')
    .controller('ReceptionController', ReceptionController);

  ReceptionController.$inject = ['$scope', 'Authentication'];

  /**
  * @namespace ReceptionController
  */
  function ReceptionController($scope, Authentication) {
    var vm = this;

    vm.isAuthenticated = isAuthenticated();

    /**
    * @name isAuthenticated
    * @desc Log the user out
    * @memberOf fcbp.layout.controllers.ReceptionController
    */
    function isAuthenticated() {
      return Authentication.isAuthenticated();
    }

  }
})();