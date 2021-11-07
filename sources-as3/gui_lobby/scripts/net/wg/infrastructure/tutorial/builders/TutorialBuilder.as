package net.wg.infrastructure.tutorial.builders
{
   import flash.display.DisplayObject;
   import flash.events.Event;
   import flash.events.EventDispatcher;
   import net.wg.data.constants.Errors;
   import net.wg.infrastructure.events.LifeCycleEvent;
   import net.wg.infrastructure.exceptions.AbstractException;
   import net.wg.infrastructure.interfaces.ITutorialBuilder;
   import net.wg.infrastructure.interfaces.IView;
   import net.wg.utils.IAssertable;
   
   public class TutorialBuilder extends EventDispatcher implements ITutorialBuilder
   {
       
      
      private var _view:IView = null;
      
      private var _asserter:IAssertable;
      
      public function TutorialBuilder()
      {
         super();
         this._asserter = App.utils.asserter;
      }
      
      public function externalUpdate() : void
      {
      }
      
      public function setView(param1:IView) : void
      {
         this._asserter.assertNotNull(param1,"view for tutorial builder" + Errors.CANT_NULL);
         this._view = param1;
         if(param1.as_config.configVO.isResizable)
         {
            param1.addEventListener(Event.RESIZE,this.onViewResizeHandler);
         }
         param1.addEventListener(LifeCycleEvent.ON_DISPOSE,this.onViewDisposeHandler);
      }
      
      public function set component(param1:DisplayObject) : void
      {
      }
      
      public function updateData(param1:Object) : void
      {
         this._asserter.assertNotNull(param1,"data for tutorial builder" + Errors.CANT_NULL);
      }
      
      public function stopEffect() : void
      {
      }
      
      public final function dispose() : void
      {
         this.onDispose();
      }
      
      protected function onDispose() : void
      {
         this._view.removeEventListener(Event.RESIZE,this.onViewResizeHandler);
         this._view.removeEventListener(LifeCycleEvent.ON_DISPOSE,this.onViewDisposeHandler);
         this._view = null;
         this._asserter = null;
      }
      
      protected function onViewResize() : void
      {
         var _loc1_:String = "onViewResize" + Errors.ABSTRACT_INVOKE;
         DebugUtils.LOG_ERROR(_loc1_);
         throw new AbstractException(_loc1_);
      }
      
      public function get view() : IView
      {
         return this._view;
      }
      
      private function onViewResizeHandler(param1:Event) : void
      {
         this.onViewResize();
      }
      
      private function onViewDisposeHandler(param1:LifeCycleEvent) : void
      {
         this.dispose();
      }
   }
}
