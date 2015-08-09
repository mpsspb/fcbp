/**
* NewClientController
* @namespace fcbp.clients.controllers
*/
(function () {
  'use strict';

  angular
    .module('fcbp.clients.controllers')
    .controller('NewClientController', NewClientController);

  NewClientController.$inject = ['$rootScope', '$scope', 'ClubCard'];

  /**
  * @namespace NewClientController
  */
  function NewClientController($rootScope, $scope, ClubCard) {
    var vm = this;

    vm.submit = submit;
    vm.clubcards = [];

    activate();

    /**
    * @name activate
    * @desc Actions to be performed when this controller is instantiated
    * @memberOf fcbp.clients.controllers.NewClientController
    */
    function activate() {

      ClubCard.list().then(clubcardsSuccessFn, clubcardsErrorFn);

      /**
      * @name clubcardsSuccessFn
      * @desc Update ClubCard array on view
      */
      function clubcardsSuccessFn(data, status, headers, config) {
        vm.clubcards = data.data;
      }

      /**
      * @name clubcardsErrorFn
      * @desc console log error
      */
      function clubcardsErrorFn(data, status, headers, config) {
        console.log(data);
      }

    }

    /**
    * @name submit
    * @desc Create a new ClubCard
    * @memberOf fcbp.clubcard.controllers.NewClientController
    */
    function submit() {

      $rootScope.$broadcast('ClubCard.created', {
        clubcard: vm.fdata,
      });

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