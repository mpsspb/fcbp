/**
* PeriodsController
* @namespace fcbp.layout.controllers
*/
(function () {
  'use strict';

  angular
    .module('fcbp.layout.controllers')
    .controller('PeriodsController', PeriodsController);

  PeriodsController.$inject = ['$scope', '$http', 'Authentication', 'Periods'];

  /**
  * @namespace PeriodsController
  */
  function PeriodsController($scope, $http, Authentication, Periods) {
    var vm = this;

    vm.isAuthenticated = isAuthenticated();
    vm.periods = [];

    activate();

    /**
    * @name activate
    * @desc Actions to be performed when this controller is instantiated
    * @memberOf fcbp.layout.controllers.PeriodsController
    */
    function activate() {

      Periods.list().then(periodsSuccessFn, periodsErrorFn);

      $scope.$on('period.created', function (event, period) {
        Periods.list().then(periodsSuccessFn, periodsErrorFn);
      });

      $scope.$on('period.created.error', function () {
        // vm.periods.shift();
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

    };

    /**
    * @name isAuthenticated
    * @desc Log the user out
    * @memberOf fcbp.layout.controllers.PeriodsController
    */
    function isAuthenticated() {
      return Authentication.isAuthenticated();
    };

  }
})();