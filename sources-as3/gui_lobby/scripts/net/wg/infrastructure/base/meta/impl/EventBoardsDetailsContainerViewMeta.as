package net.wg.infrastructure.base.meta.impl
{
   import net.wg.data.constants.Errors;
   import net.wg.gui.lobby.eventBoards.data.EventBoardsDetailsContainerVO;
   import net.wg.infrastructure.base.AbstractView;
   import net.wg.infrastructure.exceptions.AbstractException;
   
   public class EventBoardsDetailsContainerViewMeta extends AbstractView
   {
       
      
      public var closeView:Function;
      
      private var _eventBoardsDetailsContainerVO:EventBoardsDetailsContainerVO;
      
      public function EventBoardsDetailsContainerViewMeta()
      {
         super();
      }
      
      override protected function onDispose() : void
      {
         if(this._eventBoardsDetailsContainerVO)
         {
            this._eventBoardsDetailsContainerVO.dispose();
            this._eventBoardsDetailsContainerVO = null;
         }
         super.onDispose();
      }
      
      public function closeViewS() : void
      {
         App.utils.asserter.assertNotNull(this.closeView,"closeView" + Errors.CANT_NULL);
         this.closeView();
      }
      
      public final function as_setInitData(param1:Object) : void
      {
         var _loc2_:EventBoardsDetailsContainerVO = this._eventBoardsDetailsContainerVO;
         this._eventBoardsDetailsContainerVO = new EventBoardsDetailsContainerVO(param1);
         this.setInitData(this._eventBoardsDetailsContainerVO);
         if(_loc2_)
         {
            _loc2_.dispose();
         }
      }
      
      protected function setInitData(param1:EventBoardsDetailsContainerVO) : void
      {
         var _loc2_:String = "as_setInitData" + Errors.ABSTRACT_INVOKE;
         DebugUtils.LOG_ERROR(_loc2_);
         throw new AbstractException(_loc2_);
      }
   }
}
