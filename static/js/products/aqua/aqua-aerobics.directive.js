/**
* AquaAerobics
* @namespace fcbp.aquaaerobics.directives
*/
(function () {
  'use strict';

  angular
    .module('fcbp.aquaaerobics.directives')
    .directive('aquaaerobics', aquaaerobics);

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
      templateUrl: '/static/templates/products/aqua-aerobics.html?v=2'
    };

    return directive;
  }
})();