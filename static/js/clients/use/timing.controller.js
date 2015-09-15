/**
* UseTimingController
* @namespace fcbp.clients.controllers
*/
(function () {
  'use strict';

  angular
    .module('fcbp.clients.controllers')
    .controller('UseTimingController', UseTimingController);

  UseTimingController.$inject = ['$location', '$rootScope', '$routeParams', '$scope', 'Timing'];

  /**
  * @namespace UseTimingController
  */
  function UseTimingController($location, $rootScope, $routeParams, $scope, Timing) {
    var vm = this;

    vm.use = use;
    vm.fdata = {};
    activate();

    /**
    * @name activate
    * @desc Actions to be performed when this controller is instantiated
    * @memberOf fcbp.Timing.controllers.NewClubCardController
    */
    function activate() {

      var uid = $routeParams.uid
      vm.fdata = {client_timing: uid}
      Timing.get(uid).then(cardclientSuccessFn, cardclientErrorFn);

      /**
      * @name cardclientSuccessFn
      * @desc Update Timing array on view
      */
      function cardclientSuccessFn(data, status, headers, config) {
        vm.timing = data.data;
      }

      /**
      * @name cardclientErrorFn
      * @desc console log error
      */
      function cardclientErrorFn(data, status, headers, config) {
        console.log(data);
      }

    }

    /**
    * @name activate
    * @desc Actions to be performed when this controller is instantiated
    * @memberOf fcbp.Timing.controllers.NewClubCardController
    */
    function use() {

      Timing.use(vm.fdata).then(cardclientSuccessFn, cardclientErrorFn);

      /**
      * @name cardclientSuccessFn
      * @desc Update Timing array on view
      */
      function cardclientSuccessFn(data, status, headers, config) {
        activate();
        console.log('success')
      }

      /**
      * @name cardclientErrorFn
      * @desc console log error
      */
      function cardclientErrorFn(data, status, headers, config) {
        console.log(data);
      }

    }

  };

})();