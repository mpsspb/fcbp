/**
* NewClubCardController
* @namespace fcbp.clubcard.controllers
*/
(function () {
  'use strict';

  angular
    .module('fcbp.clubcard.controllers')
    .controller('NewClubCardController', NewClubCardController);

  NewClubCardController.$inject = ['$rootScope', '$scope', 'Periods', 'ClubCard'];

  /**
  * @namespace NewClubCardController
  */
  function NewClubCardController($rootScope, $scope, Periods, ClubCard) {
    var vm = this;

    vm.submit = submit;
    vm.periods = [];
    vm.fdata = {
      clients_count: 1,
      guest_training: 0,
      period_prolongation: 0,
      is_full_time: true,
    }

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

    /**
    * @name submit
    * @desc Create a new ClubCard
    * @memberOf fcbp.clubcard.controllers.NewClubCardController
    */
    function submit() {

      if (vm.fdata.is_max_visit){
        vm.fdata.max_visit = 99999
      }

      for (var key in vm.periods) {
          if (vm.fdata.period == vm.periods[key].id){
            vm.fdata.period_data = vm.periods[key];
            break;
          }
      }

      $rootScope.$broadcast('ClubCard.created',
        vm.fdata
      );

      ClubCard.create(vm.fdata).then(createClubCardSuccessFn, createClubCardErrorFn);


      /**
      * @name createClubCardSuccessFn
      * @desc Show snackbar with success message
      */
      function createClubCardSuccessFn(data, status, headers, config) {
        console.log('Success! ClubCard created.');
      }


      /**
      * @name createClubCardErrorFn
      * @desc Propogate error event and show snackbar with error message
      */
      function createClubCardErrorFn(data, status, headers, config) {
        console.log(data)
        $rootScope.$broadcast('ClubCard.created.error');
      }
    }

  }

})();