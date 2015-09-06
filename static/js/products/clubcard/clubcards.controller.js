/**
* ClubCardsController
* @namespace fcbp.clubcard.controllers
*/
(function () {
  'use strict';

  angular
    .module('fcbp.clubcard.controllers')
    .controller('ClubCardsController', ClubCardsController);

  ClubCardsController.$inject = ['$rootScope', '$scope', 'Periods', 'ClubCard'];

  /**
  * @namespace ClubCardsController
  */
  function ClubCardsController($rootScope, $scope, Periods, ClubCard) {
    var vm = this;

    vm.clubcards = [];

    activate();

    /**
    * @name activate
    * @desc Actions to be performed when this controller is instantiated
    * @memberOf fcbp.clubcard.controllers.ClubCardsController
    */
    function activate() {
      ClubCard.list().then(clubcardsSuccessFn, clubcardsErrorFn);

      $scope.$on('ClubCard.created', function (event, clubcard) {
        ClubCard.list().then(clubcardsSuccessFn, clubcardsErrorFn);
      });

      $scope.$on('ClubCard.created.error', function () {
        // vm.clubcards.shift();
      });

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
  }

})();