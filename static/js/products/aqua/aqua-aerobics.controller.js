/**
* AquaAerobicsController
* @namespace fcbp.aquaaerobics.controllers
*/
(function () {
  'use strict';

  angular
    .module('fcbp.aquaaerobics.controllers')
    .controller('AquaAerobicsController', AquaAerobicsController);

  AquaAerobicsController.$inject = ['$rootScope', '$scope', 'AquaAerobics'];

  /**
  * @namespace AquaAerobicsController
  */
  function AquaAerobicsController($rootScope, $scope, AquaAerobics) {
    var vm = this;

    vm.aquaaerobicses = [];

    activate();

    /**
    * @name activate
    * @desc Actions to be performed when this controller is instantiated
    * @memberOf fcbp.aquaaerobics.controllers.AquaAerobicsController
    */
    function activate() {
      AquaAerobics.list().then(aquaaerobicsesSuccessFn, aquaaerobicsesErrorFn);

      $scope.$on('AquaAerobics.created', function (event, aquaaerobics) {
        AquaAerobics.list().then(aquaaerobicsesSuccessFn, aquaaerobicsesErrorFn);
      });

      $scope.$on('AquaAerobics.created.error', function () {
        // vm.aquaaerobicses.shift();
      });

      /**
      * @name aquaaerobicsesSuccessFn
      * @desc Update AquaAerobics array on view
      */
      function aquaaerobicsesSuccessFn(data, status, headers, config) {
        vm.aquaaerobicses = data.data;
      }

      /**
      * @name aquaaerobicsesErrorFn
      * @desc console log error
      */
      function aquaaerobicsesErrorFn(data, status, headers, config) {
        console.log(data);
      }

    }
  }

})();