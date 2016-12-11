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

    vm.update = function(train) {
      Training.update(train.id, train).then(updSuccessFn, updErrorFn);

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