/**
* UseClientPersonalController
* @namespace fcbp.clients.controllers
*/
(function () {
  'use strict';

  angular
    .module('fcbp.clients.controllers')
    .controller('UseClientPersonalController', UseClientPersonalController);

  UseClientPersonalController.$inject = [
    '$location', '$rootScope', '$routeParams', '$scope', '$http',
    'Personals', 'Employees', 'Clients'];

  /**
  * @namespace UseClientPersonalController
  */
  function UseClientPersonalController(
    $location, $rootScope, $routeParams, $scope, $http,
    Personals, Employees, Clients) {

    var vm = this;

    vm.use = use;
    vm.set_emp = set_emp;
    vm.prolongation = prolongation;
    vm.prolongation_del = prolongation_del;

    vm.search_client = search_client;
    vm.choose_owner = choose_owner;
    vm.set_owner = set_owner;

    activate();

    /**
    * @name activate
    * @desc Actions to be performed when this controller is instantiated
    * @memberOf fcbp.clients.controllers.UseClientPersonalController
    */
    function activate() {
      vm.uid = $routeParams.uid;

      var now = moment().format('DD.MM.YYYY HH:mm')
      // forms data initial
      vm.prdata = {
        days: 1,
        amount: 0.0,
        is_paid: false,
        personal: vm.uid,
        date: now,
        payment_type: 1
      }

      vm.owner = {
        amount: 0,
        payment_type: 0
      }

      Personals.get(vm.uid).then(personalclientSuccessFn, personalclientErrorFn);

      /**
      * @name personalclientSuccessFn
      * @desc Update Personals array on view
      */
      function personalclientSuccessFn(data, status, headers, config) {
        vm.personal = data.data;
        // is free prolongation
        if (vm.personal.rest_prolongation > 0) {
          vm.free_prolongation = true
        } else {
          vm.free_prolongation = false
          vm.prdata.is_paid = true
        }
      }

      /**
      * @name personalclientErrorFn
      * @desc console log error
      */
      function personalclientErrorFn(data, status, headers, config) {
        console.log(data);
      }

      Employees.list().then(listEmployeeSuccessFn, listEmployeeErrorFn);
    
      /**
      * @name listEmployeeSuccessFn
      * @desc Show snackbar with success message
      */
      function listEmployeeSuccessFn(data, status, headers, config) {
        vm.employees = data.data;
      }


      /**
      * @name listEmployeeErrorFn
      * @desc Propogate error event and show snackbar with error message
      */
      function listEmployeeErrorFn(data, status, headers, config) {
        console.log(data)
      }

    }; // end activate

    function set_emp() {
      $http.patch('/api/v1/clients/personal/' + vm.uid + '/', vm.empdata
                ).then(set_empSuccessFn, set_empErrorFn);;

      /**
      * @name cardclientSuccessFn
      * @desc Update ClubCard array on view
      */
      function set_empSuccessFn(data, status, headers, config) {
        activate();
      }

      /**
      * @name cardclientErrorFn
      * @desc console log error
      */
      function set_empErrorFn(data, status, headers, config) {
        console.log(data);
      }
    };

    /* Search new owners clients
    */
    function search_client() {
      vm.new_owner = ""
      Clients.full_search(vm.ext).then(clntSearchSuccessFn, clntSearchErrorFn);

      function clntSearchSuccessFn(data, status, headers, config) {
          vm.findClients = data.data;
          console.log(data)
      }

      function clntSearchErrorFn(data, status, headers, config) {
          console.log(data);
      }
    };

    /*
    * Choose new owner
    */
    function choose_owner(key) {
      vm.new_owner = vm.findClients[key];
      vm.findClients = [];
    }

    /*
    * Set new owner
    */
    function set_owner() {
      Personals.ownerp({
        "client": vm.new_owner.id,
        "personal": vm.uid,
        "amount": vm.owner.amount,
        "payment_type": vm.owner.payment_type
      }).then(clntSetOwnerSuccessFn, clntSetOwnerErrorFn);

      function clntSetOwnerSuccessFn(data, status, headers, config) {
         $location.url('/cardclient/' + vm.new_owner.id);
      }

      function clntSetOwnerErrorFn(data, status, headers, config) {
        console.log(data);
      }

    };

    function prolongation() {
      Personals.prolongation(vm.prdata).then(prolongationSuccessFn, prolongationErrorFn);

      /**
      * @name prolongationSuccessFn
      * @desc Update Personals array on view
      */
      function prolongationSuccessFn(data, status, headers, config) {
        activate();
      }

      /**
      * @name prolongationErrorFn
      * @desc console log error
      */
      function prolongationErrorFn(data, status, headers, config) {
        console.log(data);
      }

    };

    function prolongation_del(uid) {
      Personals.prolongation_del(uid).then(prolongationSuccessFn, prolongationErrorFn);

      /**
      * @name prolongationSuccessFn
      * @desc Update Personals array on view
      */
      function prolongationSuccessFn(data, status, headers, config) {
        activate();
      }

      /**
      * @name prolongationErrorFn
      * @desc console log error
      */
      function prolongationErrorFn(data, status, headers, config) {
        console.log(data);
      }

    };

    function use() {

      var uid = $routeParams.uid
      var fdata = {client_personal: uid}
      Personals.use(fdata).then(personalclientSuccessFn, personalclientErrorFn);

      /**
      * @name personalclientSuccessFn
      * @desc Update Personals array on view
      */
      function personalclientSuccessFn(data, status, headers, config) {
        activate();
        console.log('success')
      }

      /**
      * @name personalclientErrorFn
      * @desc console log error
      */
      function personalclientErrorFn(data, status, headers, config) {
        console.log(data);
      }

    }

  };

})();