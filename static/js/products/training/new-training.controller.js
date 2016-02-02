/**
* NewTrainingController
* @namespace fcbp.training.controllers
*/
(function () {
  'use strict';

  angular
    .module('fcbp.training.controllers')
    .controller('NewTrainingController', NewTrainingController);

  NewTrainingController.$inject = ['$rootScope', '$scope', 'Training'];

  /**
  * @namespace NewTrainingController
  */
  function NewTrainingController($rootScope, $scope, Training) {
    var vm = this;

    vm.submit = submit;

    vm.fdata = {};

    /**
    * @name submit
    * @desc Create a new Training
    * @memberOf fcbp.training.controllers.NewTrainingController
    */
    function submit() {

      Training.create(vm.fdata).then(createTrainingSuccessFn, createTrainingErrorFn);


      /**
      * @name createTrainingSuccessFn
      * @desc Show snackbar with success message
      */
      function createTrainingSuccessFn(data, status, headers, config) {
        $rootScope.$broadcast('training.created', vm.fdata );
        console.log('Success! Training created.');
      }


      /**
      * @name createTrainingErrorFn
      * @desc Propogate error event and show snackbar with error message
      */
      function createTrainingErrorFn(data, status, headers, config) {
        console.log(data)
        $rootScope.$broadcast('training.created.error');
      }
    }

  }

})();