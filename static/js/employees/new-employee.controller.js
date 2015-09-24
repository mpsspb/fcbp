/**
* NewEmployeeController
* @namespace fcbp.employees.controllers
*/
(function () {
  'use strict';

  angular
    .module('fcbp.employees.controllers')
    .controller('NewEmployeeController', NewEmployeeController);

  NewEmployeeController.$inject = ['$scope', '$http', 'Authentication' , 'Employees'];

  /**
  * @namespace NewEmployeeController
  */
  function NewEmployeeController($scope, $http, Authentication, Employees ) {
    var vm = this;

    vm.isAuthenticated = isAuthenticated();
    vm.submit = submit

    /**
    * @name isAuthenticated
    * @desc Log the user out
    * @memberOf fcbp.employees.controllers.NewEmployeeController
    */
    function isAuthenticated() {
      return Authentication.isAuthenticated();
    };

    function submit() {
      Employees.create(vm.fdata).then(createEmployeeSuccessFn, createEmployeeErrorFn);
    
      /**
      * @name createEmployeeSuccessFn
      * @desc Show snackbar with success message
      */
      function createEmployeeSuccessFn(data, status, headers, config) {
        console.log('Success! Employee created.');
        window.location = '/#/employees-list';
      }


      /**
      * @name createEmployeeErrorFn
      * @desc Propogate error event and show snackbar with error message
      */
      function createEmployeeErrorFn(data, status, headers, config) {
        console.log(data)
        $rootScope.$broadcast('Employee.created.error');
      }

    }

  }
})();