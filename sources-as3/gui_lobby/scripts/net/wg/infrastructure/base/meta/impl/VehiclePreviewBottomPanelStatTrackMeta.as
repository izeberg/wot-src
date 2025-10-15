package net.wg.infrastructure.base.meta.impl
{
   import net.wg.data.constants.Errors;
   import net.wg.gui.lobby.vehiclePreview.data.VPStatTrackVO;
   import net.wg.infrastructure.base.BaseDAAPIComponent;
   import net.wg.infrastructure.exceptions.AbstractException;
   
   public class VehiclePreviewBottomPanelStatTrackMeta extends BaseDAAPIComponent
   {
       
      
      private var _vPStatTrackVO:VPStatTrackVO;
      
      public function VehiclePreviewBottomPanelStatTrackMeta()
      {
         super();
      }
      
      override protected function onDispose() : void
      {
         if(this._vPStatTrackVO)
         {
            this._vPStatTrackVO.dispose();
            this._vPStatTrackVO = null;
         }
         super.onDispose();
      }
      
      public final function as_setData(param1:Object) : void
      {
         var _loc2_:VPStatTrackVO = this._vPStatTrackVO;
         this._vPStatTrackVO = new VPStatTrackVO(param1);
         this.setData(this._vPStatTrackVO);
         if(_loc2_)
         {
            _loc2_.dispose();
         }
      }
      
      protected function setData(param1:VPStatTrackVO) : void
      {
         var _loc2_:String = "as_setData" + Errors.ABSTRACT_INVOKE;
         DebugUtils.LOG_ERROR(_loc2_);
         throw new AbstractException(_loc2_);
      }
   }
}
