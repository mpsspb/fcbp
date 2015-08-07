/**
* ProductsController
* @namespace fcbp.layout.controllers
*/
(function () {
  'use strict';

  angular
    .module('fcbp.layout.controllers')
    .controller('ProductsController', ProductsController);

  ProductsController.$inject = ['$scope', '$http', 'Authentication', 'Periods', 'ClubCard'];

  /**
  * @namespace ProductsController
  */
  function ProductsController($scope, $http, Authentication, Periods, ClubCard) {
    var vm = this;

    vm.isAuthenticated = isAuthenticated();
    vm.periods = [];
    vm.club_cards = [];

    activate();

    /**
    * @name activate
    * @desc Actions to be performed when this controller is instantiated
    * @memberOf fcbp.layout.controllers.ProductsController
    */
    function activate() {
      Periods.list().then(periodsSuccessFn, periodsErrorFn);
      ClubCard.list().then(club_cardsSuccessFn, club_cardsErrorFn);

      $scope.$on('period.created', function (event, period) {
        vm.periods.unshift(period);
      });

      $scope.$on('period.created.error', function () {
        vm.periods.shift();
      });

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

      /**
      * @name club_cardsSuccessFn
      * @desc Update Periods array on view
      */
      function club_cardsSuccessFn(data, status, headers, config) {
        vm.club_cards = data.data;
      }

      /**
      * @name club_cardsErrorFn
      * @desc console log error
      */
      function club_cardsErrorFn(data, status, headers, config) {
        console.log(data);
      }

    };

    /**
    * @name isAuthenticated
    * @desc Log the user out
    * @memberOf fcbp.layout.controllers.ProductsController
    */
    function isAuthenticated() {
      return Authentication.isAuthenticated();
    }

  }
})();