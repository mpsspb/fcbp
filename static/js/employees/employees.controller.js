/**
* EmployeesController
* @namespace fcbp.employees.controllers
*/
(function () {
  'use strict';

  angular
    .module('fcbp.employees.controllers')
    .controller('EmployeesController', EmployeesController);

  EmployeesController.$inject = ['$scope', '$http', 'Authentication' ];

  /**
  * @namespace EmployeesController
  */
  function EmployeesController($scope, $http, Authentication ) {
    var vm = this;

    vm.isAuthenticated = isAuthenticated();

    /**
    * @name isAuthenticated
    * @desc Log the user out
    * @memberOf fcbp.employees.controllers.EmployeesController
    */
    function isAuthenticated() {
      return Authentication.isAuthenticated();
    };

  }
})();