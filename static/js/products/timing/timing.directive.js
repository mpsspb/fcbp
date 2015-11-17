/**
* Timing
* @namespace fcbp.timing.directives
*/
(function () {
  'use strict';

  angular
    .module('fcbp.timing.directives')
    .directive('timing', timing);


  var active = function($scope, Timing) {
    var vm = this;
    vm.active = function () {
      Timing.active($scope.timing.id).then(timingSuccessFn, timingErrorFn);

      function timingSuccessFn(data, status, headers, config) {
        $scope.timing = data.data;
      }
      function timingErrorFn(data, status, headers, config) {
        console.log(data);
      }
    };
  };
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
      controller: active,
      controllerAs: 'vm',
      templateUrl: '/static/templates/products/timing.html?v=1'
    };

    return directive;
  }
})();