/**
* TrainingController
* @namespace fcbp.training.controllers
*/
(function () {
  'use strict';

  angular
    .module('fcbp.training.controllers')
    .controller('TrainingController', TrainingController);

  TrainingController.$inject = ['$scope', '$http', 'Authentication', 'Training'];

  /**
  * @namespace TrainingController
  */
  function TrainingController($scope, $http, Authentication, Training) {
    var vm = this;

    vm.isAuthenticated = isAuthenticated();
    vm.training = [];

    activate();

    /**
    * @name activate
    * @desc Actions to be performed when this controller is instantiated
    * @memberOf fcbp.training.controllers.TrainingController
    */
    function activate() {

      Training.list().then(trainingSuccessFn, trainingErrorFn);

      $scope.$on('sport.created', function (event, sport) {
        Training.list().then(trainingSuccessFn, trainingErrorFn);
      });

      $scope.$on('sport.created.error', function () {
        // vm.training.shift();
      });

      /**
      * @name trainingSuccessFn
      * @desc Update Training array on view
      */
      function trainingSuccessFn(data, status, headers, config) {
        vm.training = data.data;
      }

      /**
      * @name trainingErrorFn
      * @desc console log error
      */
      function trainingErrorFn(data, status, headers, config) {
        console.log(data);
      }

    };

    function isAuthenticated() {
      return Authentication.isAuthenticated();
    };

  }
})();