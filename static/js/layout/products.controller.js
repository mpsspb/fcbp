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
    vm.clubcards = [];

    activate();

    /**
    * @name activate
    * @desc Actions to be performed when this controller is instantiated
    * @memberOf fcbp.layout.controllers.ProductsController
    */
    function activate() {
      Periods.list().then(periodsSuccessFn, periodsErrorFn);

      $scope.$on('period.created', function (event, period) {
        vm.periods.unshift(period);
      });

      $scope.$on('period.created.error', function () {
        vm.periods.shift();
      });


      ClubCard.list().then(clubcardsSuccessFn, clubcardsErrorFn);

      $scope.$on('ClubCard.created', function (event, clubcard) {
        vm.clubcards.unshift(clubcard);
      });

      $scope.$on('ClubCard.created.error', function () {
        vm.clubcards.shift();
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

    };

    /**
    * @name isAuthenticated
    * @desc Log the user out
    * @memberOf fcbp.layout.controllers.ProductsController
    */
    function isAuthenticated() {
      return Authentication.isAuthenticated();
    };

  }
})();