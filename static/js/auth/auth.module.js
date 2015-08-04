(function () {
  'use strict';

  angular
    .module('fcbp.auth', [
      'fcbp.auth.services',
      'fcbp.auth.controllers'
    ]);

  angular
    .module('fcbp.auth.controllers', []);

  angular
    .module('fcbp.auth.services', ['ngCookies']);

})();