/**
* PositionsController
* @namespace fcbp.positions.controllers
*/
(function () {
  'use strict';

  angular
    .module('fcbp.positions.controllers')
    .controller('PositionsController', PositionsController);

  PositionsController.$inject = ['$scope', '$http', 'Authentication', 'Positions' ];

  /**
  * @namespace PositionsController
  */
  function PositionsController($scope, $http, Authentication, Positions ) {
    var vm = this;

    vm.positions = [];

    vm.isAuthenticated = isAuthenticated();

    activate();

    /**
    * @name activate
    * @desc Actions to be performed when this controller is instantiated
    * @memberOf fcbp.positions.controllers.PositionsController
    */
    function activate() {

      Positions.list().then(positionsSuccessFn, positionsErrorFn);

      $scope.$on('position.created', function (event, position) {
        Positions.list().then(positionsSuccessFn, positionsErrorFn);
      });

      $scope.$on('position.created.error', function () {
        // vm.positions.shift();
      });

      /**
      * @name positionsSuccessFn
      * @desc Update ClubCard array on view
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

    };

    /**
    * @name isAuthenticated
    * @desc Log the user out
    * @memberOf fcbp.positions.controllers.PositionsController
    */
    function isAuthenticated() {
      return Authentication.isAuthenticated();
    };

  }
})();