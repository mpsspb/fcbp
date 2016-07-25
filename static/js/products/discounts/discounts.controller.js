/**
* DiscountsController
* @namespace fcbp.discounts.controllers
*/
(function () {
  'use strict';

  angular
    .module('fcbp.discounts.controllers')
    .controller('DiscountsController', SportsController);

  SportsController.$inject = ['$scope', '$http', 'Authentication', 'Discounts'];

  /**
  * @namespace SportsController
  */
  function SportsController($scope, $http, Authentication, Discounts) {
    var vm = this;

    vm.discounts = [];

    activate();

    /**
    * @name activate
    * @desc Actions to be performed when this controller is instantiated
    * @memberOf fcbp.sports.controllers.SportsController
    */
    function activate() {

      Discounts.list().then(sportsSuccessFn, sportsErrorFn);

      $scope.$on('discount.created', function (event, sport) {
        Discounts.list().then(sportsSuccessFn, sportsErrorFn);
      });

      $scope.$on('discount.created.error', function () {
        // vm.discounts.shift();
      });

      /**
      * @name sportsSuccessFn
      * @desc Update Discounts array on view
      */
      function sportsSuccessFn(data, status, headers, config) {
        vm.discounts = data.data;
      }

      /**
      * @name sportsErrorFn
      * @desc console log error
      */
      function sportsErrorFn(data, status, headers, config) {
        console.log(data);
      }

    };

    vm.update = function(discount) {
      Discounts.update(discount.id, discount).then(updSuccessFn, updErrorFn);

      function updSuccessFn(data, status, headers, config) {
        activate();
        vm.success = true;
      }
      function updErrorFn(data, status, headers, config) {
        vm.error = true;
        vm.error_data = data.data;
        console.log(data);
      }

    }

  }
})();