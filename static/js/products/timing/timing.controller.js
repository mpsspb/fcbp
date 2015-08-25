/**
* TimingController
* @namespace fcbp.timing.controllers
*/
(function () {
  'use strict';

  angular
    .module('fcbp.timing.controllers')
    .controller('TimingController', TimingController);

  TimingController.$inject = ['$rootScope', '$scope', 'Timing'];

  /**
  * @namespace TimingController
  */
  function TimingController($rootScope, $scope, Timing) {
    var vm = this;

    vm.timings = [];

    activate();

    /**
    * @name activate
    * @desc Actions to be performed when this controller is instantiated
    * @memberOf fcbp.timing.controllers.TimingController
    */
    function activate() {
      Timing.list().then(timingSuccessFn, timingErrorFn);

      $scope.$on('Timing.created', function (event, ticket) {
        Timing.list().then(timingSuccessFn, timingErrorFn);
      });

      $scope.$on('Timing.created.error', function () {
        // 
      });

      /**
      * @name timingSuccessFn
      * @desc Update Timing array on view
      */
      function timingSuccessFn(data, status, headers, config) {
        vm.timings = data.data;
      }

      /**
      * @name timingErrorFn
      * @desc console log error
      */
      function timingErrorFn(data, status, headers, config) {
        console.log(data);
      }

    }
  }

})();