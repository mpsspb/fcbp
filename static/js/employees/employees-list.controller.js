/**
* EmployeesListController
* @namespace fcbp.employees.controllers
*/
(function () {
  'use strict';

  angular
    .module('fcbp.employees.controllers')
    .controller('EmployeesListController', EmployeesListController);

  EmployeesListController.$inject = ['$scope', '$http', 'Authentication', 'Employees'];

  /**
  * @namespace EmployeesListController
  */
  function EmployeesListController($scope, $http, Authentication, Employees ) {
    var vm = this;

    vm.isAuthenticated = isAuthenticated();

    activate();

    function activate() {
      Employees.list().then(listEmployeeSuccessFn, listEmployeeErrorFn);
    
      /**
      * @name listEmployeeSuccessFn
      * @desc Show snackbar with success message
      */
      function listEmployeeSuccessFn(data, status, headers, config) {
        vm.employess = data.data;
      }


      /**
      * @name listEmployeeErrorFn
      * @desc Propogate error event and show snackbar with error message
      */
      function listEmployeeErrorFn(data, status, headers, config) {
        console.log(data)
      }
    }

    /**
    * @name isAuthenticated
    * @desc Log the user out
    * @memberOf fcbp.employees.controllers.EmployeesListController
    */
    function isAuthenticated() {
      return Authentication.isAuthenticated();
    };

  }
})();