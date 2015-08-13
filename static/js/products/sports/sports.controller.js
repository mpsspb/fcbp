/**
* SportsController
* @namespace fcbp.sports.controllers
*/
(function () {
  'use strict';

  angular
    .module('fcbp.sports.controllers')
    .controller('SportsController', SportsController);

  SportsController.$inject = ['$scope', '$http', 'Authentication', 'Sports'];

  /**
  * @namespace SportsController
  */
  function SportsController($scope, $http, Authentication, Sports) {
    var vm = this;

    vm.isAuthenticated = isAuthenticated();
    vm.sports = [];

    activate();

    /**
    * @name activate
    * @desc Actions to be performed when this controller is instantiated
    * @memberOf fcbp.sports.controllers.SportsController
    */
    function activate() {

      Sports.list().then(sportsSuccessFn, sportsErrorFn);

      $scope.$on('sport.created', function (event, sport) {
        Sports.list().then(sportsSuccessFn, sportsErrorFn);
      });

      $scope.$on('sport.created.error', function () {
        // vm.sports.shift();
      });

      /**
      * @name sportsSuccessFn
      * @desc Update ClubCard array on view
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

    };

    /**
    * @name isAuthenticated
    * @desc Log the user out
    * @memberOf fcbp.sports.controllers.SportsController
    */
    function isAuthenticated() {
      return Authentication.isAuthenticated();
    };

  }
})();