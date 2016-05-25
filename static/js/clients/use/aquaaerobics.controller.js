/**
* UseClientAquaController
* @namespace fcbp.clients.controllers
*/
(function () {
  'use strict';

  angular
    .module('fcbp.clients.controllers')
    .controller('UseClientAquaController', UseClientAquaController);

  UseClientAquaController.$inject = ['$location', '$rootScope', '$routeParams', '$scope', 
                                     'ClientPayment', 'AquaAerobics'];

  /**
  * @namespace UseClientAquaController
  */
  function UseClientAquaController($location, $rootScope, $routeParams, $scope, 
                                   ClientPayment, AquaAerobics) {
    var vm = this;

    vm.use = use;
    vm.payment = payment;

    activate();

    /**
    * @name activate
    * @desc Actions to be performed when this controller is instantiated
    * @memberOf fcbp.AquaAerobics.controllers.NewClubAquaController
    */
    function activate() {

      var uid = $routeParams.uid
      AquaAerobics.get(uid).then(aquaclientSuccessFn, aquaclientErrorFn);

      /**
      * @name aquaclientSuccessFn
      * @desc Update AquaAerobics array on view
      */
      function aquaclientSuccessFn(data, status, headers, config) {
        vm.aqua = data.data;
      }

      /**
      * @name aquaclientErrorFn
      * @desc console log error
      */
      function aquaclientErrorFn(data, status, headers, config) {
        console.log(data);
      }

    }

    function use(out) {

      var uid = $routeParams.uid
      var fdata = {client_aqua_aerobics: uid}

      if (out) {
        AquaAerobics.use_exit(fdata).then(aquaclientSuccessFn, aquaclientErrorFn);
        return 1
      }

      AquaAerobics.use(fdata).then(aquaclientSuccessFn, aquaclientErrorFn);

      /**
      * @name aquaclientSuccessFn
      * @desc Update AquaAerobics array on view
      */
      function aquaclientSuccessFn(data, status, headers, config) {
        activate();
        console.log('success')
      }

      /**
      * @name aquaclientErrorFn
      * @desc console log error
      */
      function aquaclientErrorFn(data, status, headers, config) {
        console.log(data);
      }

    }

    // function for close credit
    function payment(payment_type, uid) {
      ClientPayment.close_credit(payment_type, uid)
                   .then(closeSuccessFn, closeErrorFn);

      /**
      * @name closeSuccessFn
      * @desc Update ClubCard array on view
      */
      function closeSuccessFn(data, status, headers, config) {
        console.log('success')
        activate()
      }

      /**
      * @name closeErrorFn
      * @desc console log error
      */
      function closeErrorFn(data, status, headers, config) {
        console.log(data);
      }

    };

  };

})();