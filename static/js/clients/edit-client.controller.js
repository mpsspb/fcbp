/**
* EditClientController
* @namespace fcbp.clients.controllers
*/
(function () {
  'use strict';

  angular
    .module('fcbp.clients.controllers')
    .controller('EditClientController', EditClientController);

  EditClientController.$inject = ['$rootScope', '$routeParams', '$scope', 'Clients'];

  /**
  * @namespace EditClientController
  */
  function EditClientController($rootScope, $routeParams, $scope, Clients) {
    var vm = this;

    vm.submit = submit;
    vm.f_mobile_toggle = f_mobile_toggle;
    vm.success = false;
    vm.error = false;
    vm.list_matches = [];
    vm.matches_show = false;
    vm.search_client = search_client;

    activate();

    /**
    * @name activate
    * @desc Actions to be performed when this controller is instantiated
    * @memberOf fcbp.clubcard.controllers.EditClientController
    */
    function activate() {

      var uid = $routeParams.uid
      Clients.get(uid).then(cardclientSuccessFn, cardclientErrorFn);

      /**
      * @name cardclientSuccessFn
      * @desc Update ClubCard array on view
      */
      function cardclientSuccessFn(data, status, headers, config) {
        vm.fdata = data.data;
        vm.fdata.born = moment(vm.fdata.born, 'YYYY-MM-DD').format('DD.MM.YYYY');
        if (vm.fdata.passport_date){
          vm.fdata.passport_date = moment(vm.fdata.passport_date, 'YYYY-MM-DD').format('DD.MM.YYYY');
        }
        if(vm.fdata.mobile) {
          vm.fdata.mobile_form = String(vm.fdata.mobile)
          if (vm.fdata.mobile_form.length < 10) {
            vm.mobile_toggle = true
          } else {
            vm.mobile_toggle = false
          }
        }
        if(vm.fdata.phone) {
          vm.fdata.phone_str = String(vm.fdata.phone)
        }
      }

      /**
      * @name cardclientErrorFn
      * @desc console log error
      */
      function cardclientErrorFn(data, status, headers, config) {
        console.log(data);
      }
    }

    function search_client() {
      Clients.exact_search(vm.fdata).then(clntSearchSuccessFn, clntSearchErrorFn);

      function clntSearchSuccessFn(data, status, headers, config) {
        if (data.data.length > 0) {
          vm.list_matches = data.data;
        } else {
          vm.list_matches = []
        };
      };

      function clntSearchErrorFn(data, status, headers, config) {
        console.log(data);
      };
    };

    function f_mobile_toggle() {
      if(vm.mobile_toggle && vm.fdata.mobile_form.length > 9){
        vm.fdata.mobile_form = vm.fdata.mobile_form.substr(3)
      }
    }
    /**
    * @name submit
    * @desc Create a new Client
    * @memberOf fcbp.client.controllers.EditClientController
    */
    function submit() {

      var numberPattern = /\d+/g;

      if (vm.fdata.mobile_form) {
        vm.fdata.mobile_form
        var mobile = vm.fdata.mobile_form.match( numberPattern );
        vm.fdata.mobile = mobile.join("");
      } else {
        vm.fdata.mobile = null
      }

      if (vm.fdata.phone_str){
        var phone = vm.fdata.phone_str.match( numberPattern );
        vm.fdata.phone = phone.join("");
      } else {
        vm.fdata.phone = null
      }

      delete vm.fdata.avatar
      delete vm.fdata.introductory_date
      delete vm.fdata.introductory_employee

      Clients.update(vm.fdata, vm.fdata.id).then(updClientSuccessFn, updClientErrorFn);


      /**
      * @name updClientSuccessFn
      * @desc Show snackbar with success message
      */
      function updClientSuccessFn(data, status, headers, config) {
        console.log('Success! Client created.');
        vm.success = true
        activate()
      }


      /**
      * @name updClientErrorFn
      * @desc Propogate error event and show snackbar with error message
      */
      function updClientErrorFn(data, status, headers, config) {
        console.log(data, status, headers, config)
        vm.error = true
        vm.error_data = data.data
        $rootScope.$broadcast('Client.created.error');
      }
    }
  };

})();