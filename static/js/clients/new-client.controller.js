/**
* NewClientController
* @namespace fcbp.clients.controllers
*/
(function () {
  'use strict';

  angular
    .module('fcbp.clients.controllers')
    .controller('NewClientController', NewClientController);

  NewClientController.$inject = ['$rootScope', '$scope', 'ClubCard'];

  /**
  * @namespace NewClientController
  */
  function NewClientController($rootScope, $scope, ClubCard) {
    var vm = this;

    vm.submit = submit;
    vm.clubcards = [];
    vm.makeSnapshot = makeSnapshot;
    vm.onSuccess = onSuccess;

    vm.myChannel = {
        // the fields below are all optional
        video: null // Will reference the video element on success
      };
    var _video = vm.myChannel.video;

    activate();

    /**
    * @name activate
    * @desc Actions to be performed when this controller is instantiated
    * @memberOf fcbp.clients.controllers.NewClientController
    */
    function activate() {

      ClubCard.list().then(clubcardsSuccessFn, clubcardsErrorFn);

      /**
      * @name clubcardsSuccessFn
      * @desc Update ClubCard array on view
      */
      function clubcardsSuccessFn(data, status, headers, config) {
        vm.clubcards = data.data;
      }

      /**
      * @name clubcardsErrorFn
      * @desc console log error
      */
      function clubcardsErrorFn(data, status, headers, config) {
        console.log(data);
      }

    }

    /**
    * @name submit
    * @desc Create a new ClubCard
    * @memberOf fcbp.clubcard.controllers.NewClientController
    */
    function submit() {

      $rootScope.$broadcast('ClubCard.created', {
        clubcard: vm.fdata,
      });

      ClubCard.create(vm.fdata).then(createPeriodSuccessFn, createPeriodErrorFn);


      /**
      * @name createPeriodSuccessFn
      * @desc Show snackbar with success message
      */
      function createPeriodSuccessFn(data, status, headers, config) {
        console.log('Success! ClubCard created.');
      }


      /**
      * @name createPeriodErrorFn
      * @desc Propogate error event and show snackbar with error message
      */
      function createPeriodErrorFn(data, status, headers, config) {
        console.log(data)
        $rootScope.$broadcast('ClubCard.created.error');
      }
    }

    function onSuccess() {
        // The video element contains the captured camera data
        _video = vm.myChannel.video;
    };
    /**
     * Make a snapshot of the camera data and show it in another canvas.
     */
    function makeSnapshot() {
      if (_video) {
          var patCanvas = document.querySelector('#snapshot');
          if (!patCanvas) return;


          patCanvas.width = _video.width;
          patCanvas.height = _video.height;
          var ctxPat = patCanvas.getContext('2d');

          var idata = getVideoData(0, 0, patCanvas.width, patCanvas.height);
          ctxPat.putImageData(idata, 0, 0);

          sendSnapshotToServer(patCanvas.toDataURL());
      }
    };

    var getVideoData = function getVideoData(x, y, w, h) {
        var hiddenCanvas = document.createElement('canvas');
        hiddenCanvas.width = _video.width;
        hiddenCanvas.height = _video.height;
        var ctx = hiddenCanvas.getContext('2d');
        ctx.drawImage(_video, 0, 0, _video.width, _video.height);
        return ctx.getImageData(x, y, w, h);
    };

    /**
     * This function could be used to send the image data
     * to a backend server that expects base64 encoded images.
     *
     * In this example, we simply store it in the scope for display.
     */
    var sendSnapshotToServer = function sendSnapshotToServer(imgBase64) {
        vm.snapshotData = imgBase64;
    };

  };

})();