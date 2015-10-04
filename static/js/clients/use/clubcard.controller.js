/**
* UseClientCardController
* @namespace fcbp.clients.controllers
*/
(function () {
  'use strict';

  angular
    .module('fcbp.clients.controllers')
    .controller('UseClientCardController', UseClientCardController);

  UseClientCardController.$inject = ['$location', '$rootScope', '$routeParams', '$scope', 'ClubCard'];

  /**
  * @namespace UseClientCardController
  */
  function UseClientCardController($location, $rootScope, $routeParams, $scope, ClubCard) {
    var vm = this;

    vm.use = use;

    vm.uid = $routeParams.uid

    vm.guest = guest;

    activate();

    /**
    * @name activate
    * @desc Actions to be performed when this controller is instantiated
    * @memberOf fcbp.clubcard.controllers.NewClubCardController
    */
    function activate() {

      var uid = $routeParams.uid
      ClubCard.get(uid).then(cardclientSuccessFn, cardclientErrorFn);

      /**
      * @name cardclientSuccessFn
      * @desc Update ClubCard array on view
      */
      function cardclientSuccessFn(data, status, headers, config) {
        vm.card = data.data;
      }

      /**
      * @name cardclientErrorFn
      * @desc console log error
      */
      function cardclientErrorFn(data, status, headers, config) {
        console.log(data);
      }

    }

    function use(out) {

      var uid = $routeParams.uid
      var fdata = {client_club_card: uid}

      if (out) {
        ClubCard.use_exit(fdata).then(cardclientSuccessFn, cardclientErrorFn);
        return 1
      }

      ClubCard.use(fdata).then(cardclientSuccessFn, cardclientErrorFn);

      /**
      * @name cardclientSuccessFn
      * @desc Update ClubCard array on view
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

    function guest() {
      var numberPattern = /\d+/g;

      if (vm.fguest.mobile_form){
        var phone = vm.fguest.mobile_form.match( numberPattern );
        vm.fguest.phone = phone.join("");
      } else {
        delete vm.fguest.phone
      }
      
      ClubCard.guest(vm.uid, vm.fguest).then(cardclientSuccessFn, cardclientErrorFn);

      /**
      * @name cardclientSuccessFn
      * @desc Update ClubCard array on view
      */
      function cardclientSuccessFn(data, status, headers, config) {
        console.log(data);
        vm.fguest = {};
        activate();
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