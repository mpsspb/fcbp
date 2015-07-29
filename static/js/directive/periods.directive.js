/**
* Periods
* @namespace fcbp.periods.directives
*/
(function () {
  'use strict';

  angular
    .module('fcbp.periods.directives')
    .directive('periods', periods);

  /**
  * @namespace Periods
  */
  function periods() {
    /**
    * @name directive
    * @desc The directive to be returned
    * @memberOf fcbp.periods.directives.Periods
    */
    var directive = {
      controller: 'PeriodsController',
      controllerAs: 'vm',
      restrict: 'E',
      scope: {
        periods: '='
      },
      templateUrl: '/static/templates/periods.html'
    };

    return directive;
  }
})();