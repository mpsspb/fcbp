/**
* AquaAerobics
* @namespace fcbp.aquaaerobics.directives
*/
(function () {
  'use strict';

  angular
    .module('fcbp.aquaaerobics.directives')
    .directive('aquaaerobics', aquaaerobics);

  var active = function($scope, AquaAerobics) {
    var vm = this;
    vm.active = function () {
      AquaAerobics.active($scope.aquaaerobics.id).then(aquaaerobicsesSuccessFn, aquaaerobicsesErrorFn);

      function aquaaerobicsesSuccessFn(data, status, headers, config) {
        $scope.aquaaerobics = data.data;
      }
      function aquaaerobicsesErrorFn(data, status, headers, config) {
        console.log(data);
      }
    };
  };
  /**
  * @namespace aquaaerobics
  */
  function aquaaerobics() {
    /**
    * @name directive
    * @desc The directive to be returned
    * @memberOf fcbp.aquaaerobics.directives.aquaaerobics
    */
    var directive = {
      restrict: 'E',
      scope: {
        aquaaerobics: '='
      },
      controller: active,
      controllerAs: 'vm',
      templateUrl: '/static/templates/products/aqua-aerobics.html?v=2'
    };

    return directive;
  }
})();