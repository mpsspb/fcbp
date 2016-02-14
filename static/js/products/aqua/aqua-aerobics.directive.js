/**
* AquaAerobics
* @namespace fcbp.aquaaerobics.directives
*/
(function () {
  'use strict';

  angular
    .module('fcbp.aquaaerobics.directives')
    .directive('aquaaerobics', aquaaerobics);

  var DirectControl = function($scope, AquaAerobics, Periods) {

    var vm = this;
    vm.success = false;
    vm.error = false;
    vm.error_data = '';

    activate();

    /**
    * @name activate
    * @desc Actions to be performed when this controller is instantiated
    * @memberOf fcbp.clubcard.controllers.NewClubCardController
    */
    function activate() {
      Periods.list().then(periodsSuccessFn, periodsErrorFn);

      /**
      * @name periodsSuccessFn
      * @desc Update ClubCard array on view
      */
      function periodsSuccessFn(data, status, headers, config) {
        vm.periods = data.data;
      }

      /**
      * @name periodsErrorFn
      * @desc console log error
      */
      function periodsErrorFn(data, status, headers, config) {
        console.log(data);
      }

    }

    vm.update = function() {
      AquaAerobics.update($scope.aqua.id, $scope.aqua).then(updSuccessFn, updErrorFn);

      function updSuccessFn(data, status, headers, config) {
        $scope.aqua = data.data;
        vm.success = true;
      }
      function updErrorFn(data, status, headers, config) {
        vm.error = true;
        vm.error_data = data.data;
        console.log(data);
      }

    }

    vm.active = function () {
      AquaAerobics.active($scope.aqua.id).then(aquaaerobicsesSuccessFn, aquaaerobicsesErrorFn);

      function aquaaerobicsesSuccessFn(data, status, headers, config) {
        $scope.aqua = data.data;
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
        aqua: '='
      },
      controller: DirectControl,
      controllerAs: 'vm',
      templateUrl: '/static/templates/products/aqua-aerobics.html?v=2'
    };

    return directive;
  }
})();