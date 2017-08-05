/**
* NewPersonalController
* @namespace fcbp.personals.controllers
*/
(function () {
  'use strict';

  angular
    .module('fcbp.personals.controllers')
    .controller('NewPersonalController', NewPersonalController);

  NewPersonalController.$inject = ['$rootScope', '$scope', 'Personals', 'Periods', 'Positions'];

  /**
  * @namespace NewPersonalController
  */
  function NewPersonalController($rootScope, $scope, Personals, Periods, Positions) {
    var vm = this;

    vm.submit = submit;
    vm.periods = [];
    vm.positions = [];

    vm.toggleSelection = toggleSelection;

    vm.fdata = {
      clients_count: 1,
      is_full_time: true,
      positions: [],
    };

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

      Positions.list().then(positionsSuccessFn, positionsErrorFn);

      /**
      * @name positionsSuccessFn
      * @desc Update Positions array on view
      */
      function positionsSuccessFn(data, status, headers, config) {
        vm.positions = data.data;
      }

      /**
      * @name positionsErrorFn
      * @desc console log error
      */
      function positionsErrorFn(data, status, headers, config) {
        console.log(data);
      }

    }

    /**
    * @name submit
    * @desc Create a new Personal
    * @memberOf fcbp.personals.controllers.NewPersonalController
    */
    function submit() {
      Personals.create(vm.fdata).then(createPersonalSuccessFn, createPersonalErrorFn);

      /**
      * @name createPersonalSuccessFn
      * @desc Show snackbar with success message
      */
      function createPersonalSuccessFn(data, status, headers, config) {
        $rootScope.$broadcast('personal.created', vm.fdata );
        console.log('Success! Personal created.');
        vm.fdata = {
          clients_count: 1,
          is_full_time: true,
          positions: [],
        };

        angular.forEach(vm.positions, function (position) {
            position.selected = false;
        });
      }


      /**
      * @name createPersonalErrorFn
      * @desc Propogate error event and show snackbar with error message
      */
      function createPersonalErrorFn(data, status, headers, config) {
        console.log(data)
        $rootScope.$broadcast('personal.created.error');
      }
    }

    // toggle selection for a given position by name
    function toggleSelection(position) {
      console.log()
      var idx = vm.fdata.positions.indexOf(position);

      // is currently selected
      if (idx > -1) {
        vm.fdata.positions.splice(idx, 1);
      }

      // is newly selected
      else {
        vm.fdata.positions.push(position);
      }
    };

  }

})();