/**
* NewAquaAerobicsController
* @namespace fcbp.aquaaerobics.controllers
*/
(function () {
  'use strict';

  angular
    .module('fcbp.aquaaerobics.controllers')
    .controller('NewAquaAerobicsController', NewAquaAerobicsController);

  NewAquaAerobicsController.$inject = ['$rootScope', '$scope', 'Periods', 'AquaAerobics'];

  /**
  * @namespace NewAquaAerobicsController
  */
  function NewAquaAerobicsController($rootScope, $scope, Periods, AquaAerobics) {
    var vm = this;

    vm.submit = submit;
    vm.periods = [];
    vm.fdata = {
      clients_count: 1,
      period_prolongation: 0,
      is_full_time: true,
    }

    activate();

    /**
    * @name activate
    * @desc Actions to be performed when this controller is instantiated
    * @memberOf fcbp.aquaaerobics.controllers.NewAquaAerobicsController
    */
    function activate() {
      Periods.list().then(periodsSuccessFn, periodsErrorFn);

      /**
      * @name periodsSuccessFn
      * @desc Update AquaAerobics array on view
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

    }

    /**
    * @name submit
    * @desc Create a new AquaAerobics
    * @memberOf fcbp.aquaaerobics.controllers.NewAquaAerobicsController
    */
    function submit() {

      for (var key in vm.periods) {
          if (vm.fdata.period == vm.periods[key].id){
            vm.fdata.period_data = vm.periods[key];
            break;
          }
      }

      $rootScope.$broadcast('AquaAerobics.created',
        vm.fdata
      );

      AquaAerobics.create(vm.fdata).then(createAquaAerobicsSuccessFn, createAquaAerobicsErrorFn);


      /**
      * @name createAquaAerobicsSuccessFn
      * @desc Show snackbar with success message
      */
      function createAquaAerobicsSuccessFn(data, status, headers, config) {
        console.log('Success! AquaAerobics created.');
      }


      /**
      * @name createAquaAerobicsErrorFn
      * @desc Propogate error event and show snackbar with error message
      */
      function createAquaAerobicsErrorFn(data, status, headers, config) {
        console.log(data)
        $rootScope.$broadcast('AquaAerobics.created.error');
      }
    }

  }

})();