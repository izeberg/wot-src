package net.wg.story_mode.infrastructure.base.meta
{
   import flash.events.IEventDispatcher;
   
   public interface IIntroVideoMeta extends IEventDispatcher
   {
       
      
      function onVideoStartedS() : void;
      
      function onVideoCompleteS() : void;
      
      function onSkipButtonVisibleS() : void;
      
      function onSkipButtonClickedS() : void;
      
      function as_setData(param1:Object) : void;
      
      function as_setCurrentSubtitle(param1:String) : void;
      
      function as_loaded() : void;
      
      function as_pausePlayback() : void;
      
      function as_resumePlayback() : void;
      
      function as_handleKeydown() : void;
   }
}
