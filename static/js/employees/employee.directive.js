/**
* Employee
* @namespace fcbp.employee.directives
*/
(function () {
  'use strict';

  angular
    .module('fcbp.employee.directives')
    .directive('employee', employee);

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
      scope: {
        employee: '='
      },
      templateUrl: '/static/templates/employees/employee.html?08'
    };

    return directive;
  }
})();