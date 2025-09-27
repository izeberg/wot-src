package net.wg.portal.gui.battle.fullStats.components
{
   import net.wg.data.constants.Linkages;
   import net.wg.gui.components.containers.GroupEx;
   import net.wg.gui.components.containers.VerticalGroupLayout;
   import net.wg.utils.StageBreakPointList;
   
   public class MinimapItemsInfo extends GroupEx
   {
      
      private static const MINIMAP_ITEMS_LIST_GAP:int = -20;
      
      private static const MINIMAP_ITEMS_LIST_GAP_SMALL:int = -2;
       
      
      private var _minimapItemsLayout:VerticalGroupLayout = null;
      
      private var _minimapItemsLayoutSmall:VerticalGroupLayout = null;
      
      public function MinimapItemsInfo()
      {
         super();
      }
      
      override protected function initialize() : void
      {
         super.initialize();
         this._minimapItemsLayout = new VerticalGroupLayout();
         this._minimapItemsLayout.gap = MINIMAP_ITEMS_LIST_GAP;
         this._minimapItemsLayoutSmall = new VerticalGroupLayout();
         this._minimapItemsLayoutSmall.gap = MINIMAP_ITEMS_LIST_GAP_SMALL;
      }
      
      override protected function onDispose() : void
      {
         this._minimapItemsLayout.dispose();
         this._minimapItemsLayout = null;
         this._minimapItemsLayoutSmall.dispose();
         this._minimapItemsLayoutSmall = null;
         super.onDispose();
      }
      
      public function updateStageSize(param1:Number, param2:Number) : void
      {
         switch(App.stageSizeMgr.currentBreakPoint)
         {
            case StageBreakPointList.SMALL:
               itemRendererLinkage = Linkages.MINIMAP_LEGEND_ITEM_RENDERER_SMALL;
               layout = this._minimapItemsLayoutSmall;
               break;
            case StageBreakPointList.MEDIUM:
               itemRendererLinkage = Linkages.MINIMAP_LEGEND_ITEM_RENDERER_SMALL;
               layout = this._minimapItemsLayoutSmall;
               break;
            case StageBreakPointList.LARGE:
               itemRendererLinkage = Linkages.MINIMAP_LEGEND_ITEM_RENDERER;
               layout = this._minimapItemsLayout;
               break;
            case StageBreakPointList.EXTRA_LARGE:
               itemRendererLinkage = Linkages.MINIMAP_LEGEND_ITEM_RENDERER;
               layout = this._minimapItemsLayout;
               break;
            default:
               itemRendererLinkage = Linkages.MINIMAP_LEGEND_ITEM_RENDERER_SMALL;
               layout = this._minimapItemsLayoutSmall;
         }
         this.cleanUpRenderers();
         invalidateData();
      }
      
      private function cleanUpRenderers() : void
      {
         removeAllChildren(true);
         if(renderers)
         {
            renderers.splice(0,renderers.length);
         }
      }
   }
}
