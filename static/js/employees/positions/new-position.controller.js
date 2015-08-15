/**
* NewPositionController
* @namespace fcbp.positions.controllers
*/
(function () {
  'use strict';

  angular
    .module('fcbp.positions.controllers')
    .controller('NewPositionController', NewPositionController);

  NewPositionController.$inject = ['$rootScope', '$scope', 'Positions'];

  /**
  * @namespace NewPositionController
  */
  function NewPositionController($rootScope, $scope, Positions) {
    var vm = this;

    vm.submit = submit;

    vm.fdata = {};

    /**
    * @name submit
    * @desc Create a new Position
    * @memberOf fcbp.positions.controllers.NewPositionController
    */
    function submit() {

      Positions.create(vm.fdata).then(createPositionSuccessFn, createPositionErrorFn);


      /**
      * @name createPositionSuccessFn
      * @desc Show snackbar with success message
      */
      function createPositionSuccessFn(data, status, headers, config) {
        $rootScope.$broadcast('position.created', vm.fdata );
        console.log('Success! Position created.');
      }


      /**
      * @name createPositionErrorFn
      * @desc Propogate error event and show snackbar with error message
      */
      function createPositionErrorFn(data, status, headers, config) {
        console.log(data)
        $rootScope.$broadcast('position.created.error');
      }
    }

  }

})();