/**
* StartController
* @namespace fcbp.layout.controllers
*/
(function () {
  'use strict';

  angular
    .module('fcbp.layout.controllers')
    .controller('StartController', StartController);

  StartController.$inject = ['$scope', 'Authentication'];

  /**
  * @namespace StartController
  */
  function StartController($scope, Authentication) {
    var vm = this;

    vm.isAuthenticated = isAuthenticated();

    /**
    * @name isAuthenticated
    * @desc Log the user out
    * @memberOf fcbp.layout.controllers.StartController
    */
    function isAuthenticated() {
      return Authentication.isAuthenticated();
    }

  }
})();