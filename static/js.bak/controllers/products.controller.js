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
    vm.periods = Periods.list

    /**
     * @name isAdmin
     * @desc Return the currently user is admin
     * @returns {true|false}
     * @memberOf fcbp.layout.controllers.ProductsController
     */
    function isAdmin() {
      var user = $cookies.getObject('authenticatedAccount');
      if ( user && user.username == 'admin' ) {
        return true;
      }

      return false;
    }

  }
})();