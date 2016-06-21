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
                                     '$http', 'ClientPayment', 'AquaAerobics'];

  /**
  * @namespace UseClientAquaController
  */
  function UseClientAquaController($location, $rootScope, $routeParams, $scope, $http,
                                   ClientPayment, AquaAerobics) {
    var vm = this;

    vm.uid = $routeParams.uid;
    vm.use = use;
    vm.payment = payment;
    vm.freeze = freeze;
    vm.prolongation = prolongation;
    vm.paid_activate = paid_activate;
    vm.to_archive = to_archive;

    activate();

    /**
    * @name activate
    * @desc Actions to be performed when this controller is instantiated
    * @memberOf fcbp.AquaAerobics.controllers.NewClubAquaController
    */
    function activate() {

      AquaAerobics.get(vm.uid).then(aquaclientSuccessFn, aquaclientErrorFn);

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

      // freeze data
      vm.frdata = {
        days: 1,
        amount: 0.0,
        is_paid: false,
        client_aqua: vm.uid,
        fdate: moment().format('DD.MM.YYYY'),
        is_credit: false
      }
      //  paid activate data
      vm.padata = {
        is_paid_activate: true,
        paid_activate_amount: 0,
      }
      // forms prolongation data
      var now = moment().format('DD.MM.YYYY HH:mm')
      vm.prdata = {
        days: 1,
        amount: 0.0,
        is_paid: false,
        client_aqua: vm.uid,
        date: now
      }
      //  to archive data
      vm.ardata = {
        status: 0,
        block_comment: ''
      }
    }

    function use(out) {

      var fdata = {client_aqua_aerobics: vm.uid}

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

    };


    function to_archive() {

      $http.put('/api/v1/clients/aquaaerobics/' + vm.uid + '/', vm.ardata
                ).then(to_archiveSuccessFn, to_archiveErrorFn);

      /**
      * @name to_archiveSuccessFn
      * @desc Update ClubCard array on view
      */
      function to_archiveSuccessFn(data, status, headers, config) {
        window.location = '/#/archive/aquaaerobics/' + vm.uid
      }
      /**
      * @name to_archiveErrorFn
      * @desc console log error
      */
      function to_archiveErrorFn(data, status, headers, config) {
        console.log(data);
      }
    };

    function freeze() {

      if ( vm.frdata.is_credit ) {
        var credit_date = moment().add(1, 'days').startOf('day').format('DD.MM.YYYY');
        vm.frdata.schedule = credit_date;
        vm.frdata.discount = 0;
        vm.frdata.count = 1;
      }

      AquaAerobics.freeze(vm.uid, vm.frdata).then(freezeSuccessFn, freezeErrorFn);

      /**
      * @name freezeSuccessFn
      * @desc Update AquaAerobics array on view
      */
      function freezeSuccessFn(data, status, headers, config) {
        console.log(data);
        activate();
      }

      /**
      * @name freezeErrorFn
      * @desc console log error
      */
      function freezeErrorFn(data, status, headers, config) {
        console.log(data);
      }
    };

    function prolongation() {
      AquaAerobics.prolongation(vm.prdata).then(prolongationSuccessFn, prolongationErrorFn);

      /**
      * @name prolongationSuccessFn
      * @desc Update AquaAerobics array on view
      */
      function prolongationSuccessFn(data, status, headers, config) {
        console.log(data);
        vm.prdata = {
          days: 1,
          amount: 0.0,
          is_paid: false,
          client_aqua: vm.uid
        }
        activate();
      }

      /**
      * @name prolongationErrorFn
      * @desc console log error
      */
      function prolongationErrorFn(data, status, headers, config) {
        console.log(data);
      }

    }

    function paid_activate() {

      $http.put('/api/v1/clients/aquaaerobics/' + vm.uid + '/', vm.padata
                ).then(paid_activateSuccessFn, paid_activateErrorFn);

      /**
      * @name paid_activateSuccessFn
      * @desc Update AquaAerobics array on view
      */
      function paid_activateSuccessFn(data, status, headers, config) {
        window.location = '#/archive/aquaaerobics/' + vm.uid + '/';
        activate();
      }

      /**
      * @name paid_activateErrorFn
      * @desc console log error
      */
      function paid_activateErrorFn(data, status, headers, config) {
        console.log(data);
      }
    };

    // function for close credit
    function payment(payment_type, uid) {
      ClientPayment.close_credit(payment_type, uid)
                   .then(closeSuccessFn, closeErrorFn);

      /**
      * @name closeSuccessFn
      * @desc Update AquaAerobics array on view
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