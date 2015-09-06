/**
* NewTicketsController
* @namespace fcbp.Tickets.controllers
*/
(function () {
  'use strict';

  angular
    .module('fcbp.tickets.controllers')
    .controller('NewTicketsController', NewTicketsController);

  NewTicketsController.$inject = ['$rootScope', '$scope', 'Periods', 'Sports', 'Tickets'];

  /**
  * @namespace NewTicketsController
  */
  function NewTicketsController($rootScope, $scope, Periods, Sports, Tickets) {
    var vm = this;

    vm.submit = submit;
    vm.periods = [];
    vm.sports = [];
    vm.fdata = {
      period_prolongation: 0,
      is_full_time: true,
    }

    activate();

    /**
    * @name activate
    * @desc Actions to be performed when this controller is instantiated
    * @memberOf fcbp.Tickets.controllers.NewTicketsController
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

      Sports.list().then(sportsSuccessFn, sportsErrorFn);

      /**
      * @name sportsSuccessFn
      * @desc Update Tickets array on view
      */
      function sportsSuccessFn(data, status, headers, config) {
        vm.sports = data.data;
      }

      /**
      * @name sportsErrorFn
      * @desc console log error
      */
      function sportsErrorFn(data, status, headers, config) {
        console.log(data);
      }

    }

    /**
    * @name submit
    * @desc Create a new Tickets
    * @memberOf fcbp.tickets.controllers.NewTicketsController
    */
    function submit() {

      for (var key in vm.periods) {
          if (vm.fdata.period == vm.periods[key].id){
            vm.fdata.period_data = vm.periods[key];
            break;
          }
      }

      for (var key in vm.sports) {
          if (vm.fdata.sport == vm.sports[key].id){
            vm.fdata.sport_data = vm.sports[key];
            break;
          }
      }

      Tickets.create(vm.fdata).then(createticketsSuccessFn, createticketsErrorFn);


      /**
      * @name createticketsSuccessFn
      * @desc Show snackbar with success message
      */
      function createticketsSuccessFn(data, status, headers, config) {
        console.log('Success! Tickets created.');
        $rootScope.$broadcast('Tickets.created',
          vm.fdata
        );
        vm.fdata = {
          period_prolongation: 0,
          is_full_time: true,
        }
      }


      /**
      * @name createticketsErrorFn
      * @desc Propogate error event and show snackbar with error message
      */
      function createticketsErrorFn(data, status, headers, config) {
        console.log(data)
        $rootScope.$broadcast('Tickets.created.error');
      }
    }

  }

})();