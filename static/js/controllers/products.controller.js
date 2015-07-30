/**
* ProductsController
* @namespace fcbp.layout.controllers
*/
(function () {
  'use strict';

  angular
    .module('fcbp.layout.controllers')
    .controller('ProductsController', ProductsController);

  ProductsController.$inject = ['$cookies', 'Periods'];
  /**
  * @namespace ProductsController
  */
  function ProductsController($cookies, Periods) {
    var vm = this;

    vm.isAdmin = isAdmin
    vm.newPeriod = Periods.create

    /**
     * @name isAdmin
     * @desc Return the currently user is admin
     * @returns {true|false}
     * @memberOf fcbp.authentication.services.Authentication
     */
    function isAdmin() {
      var user = $cookies.getObject('authenticatedAccount');
      if ( user && user.username == 'admin' ) {
        return true;
      }

      return false;
    }

    /**
     * @name periods
     * @desc Return the currently user is admin
     * @returns {true|false}
     * @memberOf fcbp.authentication.services.Authentication
     */
    function periods() {

    }

  }
})();