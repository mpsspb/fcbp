/**
* NewTimingController
* @namespace fcbp.timing.controllers
*/
(function () {
  'use strict';

  angular
    .module('fcbp.timing.controllers')
    .controller('NewTimingController', NewTimingController);

  NewTimingController.$inject = ['$rootScope', '$scope', 'Periods', 'Timing'];

  /**
  * @namespace NewTimingController
  */
  function NewTimingController($rootScope, $scope, Periods, Timing) {
    var vm = this;

    vm.submit = submit;
    vm.periods = [];
    vm.fdata = {
      period_prolongation: 0,
      period_freeze: 0,
      clients_count: 1,
      minutes: 1,
    }
    
    activate();

    /**
    * @name activate
    * @desc Actions to be performed when this controller is instantiated
    * @memberOf fcbp.Timing.controllers.NewTimingController
    */
    function activate() {
      Periods.list().then(periodsSuccessFn, periodsErrorFn);

      /**
      * @name periodsSuccessFn
      * @desc Update Periods array on view
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

    /**
    * @name submit
    * @desc Create a new Timing
    * @memberOf fcbp.Timing.controllers.NewTimingController
    */
    function submit() {

      for (var key in vm.periods) {
          if (vm.fdata.period == vm.periods[key].id){
            vm.fdata.period_data = vm.periods[key];
            break;
          }
      }

      Timing.create(vm.fdata).then(createtimingSuccessFn, createtimingErrorFn);


      /**
      * @name createtimingSuccessFn
      * @desc Show snackbar with success message
      */
      function createtimingSuccessFn(data, status, headers, config) {
        console.log('Success! Timing created.');
        $rootScope.$broadcast('Timing.created',
          vm.fdata
        );
        // reset fdata
        vm.fdata = {
          period_prolongation: 0,
          period_freeze: 0,
          clients_count: 1,
          minutes: 1,
        }
      }


      /**
      * @name createtimingErrorFn
      * @desc Propogate error event and show snackbar with error message
      */
      function createtimingErrorFn(data, status, headers, config) {
        console.log(data)
        $rootScope.$broadcast('Timing.created.error');
      }
    }

  }

})();