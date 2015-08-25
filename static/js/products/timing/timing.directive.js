/**
* Timing
* @namespace fcbp.timing.directives
*/
(function () {
  'use strict';

  angular
    .module('fcbp.timing.directives')
    .directive('timing', timing);

  /**
  * @namespace timing
  */
  function timing() {
    /**
    * @name directive
    * @desc The directive to be returned
    * @memberOf fcbp.timing.directives.timing
    */
    var directive = {
      restrict: 'E',
      scope: {
        timing: '='
      },
      templateUrl: '/static/templates/products/timing.html?v=1'
    };

    return directive;
  }
})();