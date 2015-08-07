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

    activate();

    /**
    * @name activate
    * @desc Actions to be performed when this controller is instantiated
    * @memberOf fcbp.layout.controllers.ProductsController
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

      $rootScope.$broadcast('ClubCard.created', {
        clubcard: vm.fdata,
      });

      if (vm.fdata.is_max_visit){
        vm.fdata.is_max_visit = 99999
      }

      ClubCard.create(vm.fdata).then(createPeriodSuccessFn, createPeriodErrorFn);


      /**
      * @name createPeriodSuccessFn
      * @desc Show snackbar with success message
      */
      function createPeriodSuccessFn(data, status, headers, config) {
        console.log('Success! ClubCard created.');
      }


      /**
      * @name createPeriodErrorFn
      * @desc Propogate error event and show snackbar with error message
      */
      function createPeriodErrorFn(data, status, headers, config) {
        console.log(data)
        $rootScope.$broadcast('ClubCard.created.error');
      }
    }

  }

})();