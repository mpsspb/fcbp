/**
* Employee
* @namespace fcbp.employee.directives
*/
(function () {
  'use strict';

  angular
    .module('fcbp.employee.directives')
    .directive('employee', employee);

  var DirectControl = function($scope, Employees) {
    var vm = this;

    vm.active = function () {
      
      Employees.active($scope.employee.id).then(empSuccessFn, empErrorFn);

      function empSuccessFn(data, status, headers, config) {
        $scope.employee = data.data;
      }
      function empErrorFn(data, status, headers, config) {
        console.log(data);
      }
    };
  }
  /**
  * @namespace Employee
  */
  function employee() {
    /**
    * @name directive
    * @desc The directive to be returned
    * @memberOf fcbp.employee.directives.employee
    */
    var directive = {
      restrict: 'E',
      controller: DirectControl,
      controllerAs: 'vm',
      scope: {
        employee: '='
      },
      templateUrl: '/static/templates/employees/employee.html?09'
    };

    return directive;
  }
})();